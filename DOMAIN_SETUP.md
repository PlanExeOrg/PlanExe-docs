# Setting up docs.planexe.org with Hostinger

This guide explains how to configure the `docs.planexe.org` subdomain in Hostinger to point to GitHub Pages.

## Prerequisites

- Access to Hostinger DNS management
- GitHub repository with Pages enabled
- The repository should be `PlanExeOrg/PlanExe-docs`

## Step 1: Get GitHub Pages URL

First, you need to find your GitHub Pages URL. After deploying to GitHub Pages, it will be:
- `https://planexeorg.github.io/PlanExe-docs/` (if using the default GitHub Pages URL)

Or check your repository settings:
1. Go to `https://github.com/PlanExeOrg/PlanExe-docs/settings/pages`
2. Note the GitHub Pages URL shown there

## Step 2: Configure DNS in Hostinger

1. **Log in to Hostinger**
   - Go to [hpanel.hostinger.com](https://hpanel.hostinger.com)
   - Navigate to your domain management

2. **Access DNS Management**
   - Find your domain `planexe.org`
   - Click on "DNS / Name Servers" or "DNS Zone Editor"

3. **Add CNAME Record**
   - Click "Add Record" or "Add DNS Record"
   - Select record type: **CNAME**
   - **Name/Host**: `docs`
   - **Value/Target**: `planexeorg.github.io` (or your GitHub Pages URL without https://)
   - **TTL**: 3600 (or leave default)
   - Click "Save" or "Add Record"

   The record should look like:
   ```
   Type: CNAME
   Name: docs
   Value: planexeorg.github.io
   TTL: 3600
   ```

## Step 3: Configure GitHub Pages Custom Domain

1. **Go to Repository Settings**
   - Navigate to `https://github.com/PlanExeOrg/PlanExe-docs/settings/pages`

2. **Add Custom Domain**
   - In the "Custom domain" section, enter: `docs.planexe.org`
   - Click "Save"
   - GitHub will automatically create a CNAME file (though our workflow already handles this)

3. **Enable Enforce HTTPS** (recommended)
   - Check the "Enforce HTTPS" checkbox
   - This may take a few minutes to become available

## Step 4: Verify DNS Propagation

DNS changes can take up to 48 hours to propagate, but usually happen within a few hours.

To check if DNS is working:

```bash
# Check CNAME record
dig docs.planexe.org CNAME

# Or use nslookup
nslookup docs.planexe.org
```

You should see the CNAME pointing to `planexeorg.github.io` or similar.

## Step 5: Test the Domain

Once DNS has propagated:

1. Visit `https://docs.planexe.org` in your browser
2. You should see your documentation site
3. Check that HTTPS is working (the lock icon in the browser)

## Troubleshooting

### DNS Not Propagating

- Wait 24-48 hours for full propagation
- Clear your DNS cache: `sudo dscacheutil -flushcache` (macOS) or `ipconfig /flushdns` (Windows)
- Try using a different DNS server (e.g., Google's 8.8.8.8)

### "Certificate not yet issued" / Enforce HTTPS unavailable

If GitHub shows **Enforce HTTPS — Unavailable for your site because a certificate has not yet been issued**, do the following.

1. **Check DNS for the subdomain**  
   For `docs.planexe.org` you must have **exactly one** CNAME record:
   - **Name**: `docs` (so the full name is `docs.planexe.org`)
   - **Value**: `planexeorg.github.io` (no `https://`, no trailing slash)
   - No A, AAAA, ALIAS, or ANAME records for `docs` — extra records can block certificate issuance. See [GitHub: Verifying the DNS configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#verifying-the-dns-configuration).

2. **Restart certificate provisioning**  
   In [PlanExe-docs Pages settings](https://github.com/PlanExeOrg/PlanExe-docs/settings/pages):
   - Click **Remove** next to the custom domain `docs.planexe.org`.
   - Enter `docs.planexe.org` again and click **Save**.  
   This restarts the DNS check and Let's Encrypt certificate request. See [GitHub: Certificate not yet created](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https#troubleshooting-certificate-provisioning-certificate-not-yet-created-error).

3. **Wait**  
   Provisioning can take from a few minutes up to an hour. When a check mark appears next to your custom domain, **Enforce HTTPS** will become available — turn it on.

### SSL Certificate Issues (general)

- GitHub Pages automatically provisions SSL certificates via Let's Encrypt
- This can take a few minutes to a few hours after the domain is verified
- Make sure "Enforce HTTPS" is enabled in GitHub Pages settings once the certificate is issued

### CNAME Already Exists

- If you see an error about CNAME already existing, check your DNS records
- You might need to remove an old A record or CNAME record first
- GitHub Pages requires a CNAME record, not an A record for subdomains

### GitHub Pages Not Updating

- Check that the GitHub Actions workflow completed successfully
- Verify the `gh-pages` branch exists and has content
- Check repository settings to ensure Pages is enabled and pointing to the correct branch

## Current Configuration

The repository is already configured with:
- **GitHub Actions workflow** (`.github/workflows/deploy.yml`) that automatically creates the CNAME file
- **MkDocs configuration** (`mkdocs.yml`) with `site_url: https://docs.planexe.org`

Once DNS is configured in Hostinger, everything should work automatically!

## Additional Notes

- The GitHub Actions workflow uses `peaceiris/actions-gh-pages@v3` which automatically handles the CNAME file
- The CNAME file will be created in the `gh-pages` branch root with content: `docs.planexe.org`
- You don't need to manually create the CNAME file - the workflow handles it
