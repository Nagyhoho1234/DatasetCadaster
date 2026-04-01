# Deployment Guide

Dataset Cadaster is a purely static web application. It requires no server-side processing, no database, and no build step. Any host that can serve HTML, CSS, JS, and JSON files will work.

***

## Option A: GitHub Pages (Simplest)

This is the recommended approach for most users.

### Steps

1. Push the repository to GitHub
2. Go to **Settings > Pages**
3. Under **Source**, select **Deploy from a branch**
4. Choose the branch (e.g., `main`) and set the folder to `/app`
5. Click **Save**
6. Your site will be live at `https://<username>.github.io/DatasetCadaster/`

### Notes

- GitHub Pages serves from the `/app` directory, so all HTML pages are accessible at the root URL
- The `datasets.json` and `datasets-summary.json` files are in the repository root, **not** in `/app`. You may need to adjust paths or copy/symlink these files into `/app` depending on your setup
- GitHub Actions (price monitor, health check) will work automatically once the repository is on GitHub
- Custom domain: Settings > Pages > Custom domain. Add a CNAME record pointing to `<username>.github.io`

***

## Option B: Custom Server

If you host on your own server (e.g., `teszt1.szarazodas.stream`):

### With Nginx

```nginx
server {
    listen 80;
    server_name teszt1.szarazodas.stream;

    root /var/www/dataset-cadaster/app;
    index landing.html;

    # Serve JSON data files from the repository root
    location ~ ^/(datasets\.json|datasets-summary\.json|pricing\.json|related\.json) {
        root /var/www/dataset-cadaster;
        add_header Access-Control-Allow-Origin *;
    }

    # Cache static assets
    location ~* \.(css|js|svg|png|ico|json)$ {
        expires 1d;
        add_header Cache-Control "public, immutable";
    }

    # SPA-like fallback (not strictly needed, but nice for bookmarks)
    location / {
        try_files $uri $uri/ /landing.html;
    }
}
```

### With Apache

```apache
<VirtualHost *:80>
    ServerName teszt1.szarazodas.stream
    DocumentRoot /var/www/dataset-cadaster/app

    Alias /datasets.json /var/www/dataset-cadaster/datasets.json
    Alias /datasets-summary.json /var/www/dataset-cadaster/datasets-summary.json
    Alias /pricing.json /var/www/dataset-cadaster/pricing.json
    Alias /related.json /var/www/dataset-cadaster/related.json

    <Directory /var/www/dataset-cadaster/app>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

### With Python (development)

```bash
cd DatasetCadaster
python -m http.server 8000 --directory app
# Visit http://localhost:8000/landing.html
```

### Deployment Script

```bash
#!/bin/bash
# deploy.sh -- pull latest and restart
cd /var/www/dataset-cadaster
git pull origin main
# No build step needed -- files are served directly
echo "Deployed at $(date)"
```

***

## Option C: Cloudflare Pages / Netlify

### Cloudflare Pages

1. Connect your GitHub repository in the Cloudflare dashboard
2. Set **Build command** to (leave empty -- no build needed)
3. Set **Build output directory** to `app`
4. Deploy

Note: JSON data files in the root directory need to be accessible. You may need a `_redirects` file or adjust your `fetch()` paths to point to the correct location.

### Netlify

1. Connect your GitHub repository in the Netlify dashboard
2. Set **Build command** to (leave empty)
3. Set **Publish directory** to `app`
4. Deploy

Add a `netlify.toml` in the repository root if you need redirects:

```toml
[build]
  publish = "app"

[[redirects]]
  from = "/datasets.json"
  to = "/datasets.json"
  status = 200

[[headers]]
  for = "/*.json"
  [headers.values]
    Access-Control-Allow-Origin = "*"
```

***

## DNS Setup

If using a custom domain (e.g., `teszt1.szarazodas.stream`):

| Record Type | Host | Value |
|------------|------|-------|
| **CNAME** | `teszt1` | `<username>.github.io` (for GitHub Pages) |
| **A** | `teszt1` | Your server IP (for custom server) |
| **CNAME** | `teszt1` | `<project>.pages.dev` (for Cloudflare Pages) |

If using Cloudflare as DNS proxy (orange cloud), SSL is handled automatically.

***

## SSL Considerations

| Host | SSL |
|------|-----|
| GitHub Pages | Automatic (Let's Encrypt). Enforced via Settings > Pages > Enforce HTTPS |
| Cloudflare Pages | Automatic |
| Netlify | Automatic (Let's Encrypt) |
| Custom server | Use [Certbot](https://certbot.eff.org/) with Let's Encrypt: `sudo certbot --nginx -d teszt1.szarazodas.stream` |

For custom servers, set up auto-renewal:

```bash
sudo certbot renew --dry-run   # test
# Certbot installs a cron/systemd timer automatically
```

***

## Updating After Deployment

Since there is no build step, updating is simply:

```bash
git pull origin main
```

The GitHub Actions workflow automatically updates `pricing.json` and `health.json` every week. If you are mirroring to a custom server, set up a cron job to pull regularly:

```bash
# /etc/cron.d/dataset-cadaster
0 */6 * * * www-data cd /var/www/dataset-cadaster && git pull origin main
```
