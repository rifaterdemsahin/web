# DNS Migration Instructions: rifaterdemsahin.com

Based on your current DNS records, here is exactly what you need to change in your Cloudflare dashboard to move from WordPress to GitHub Pages while keeping your homelab and email intact.

## 🛑 1. Records to DELETE
Remove the old WordPress.com hosting records.

| Type | Name | Content | Rationale |
| :--- | :--- | :--- | :--- |
| **A** | `rifaterdemsahin.com` | `192.0.78.25` | Old WordPress IP |
| **A** | `rifaterdemsahin.com` | `192.0.78.24` | Old WordPress IP |

---

## ✅ 2. Records to ADD
Add the GitHub Pages IP addresses for the apex domain.

| Type | Name | Content | Proxy Status |
| :--- | :--- | :--- | :--- |
| **A** | `@` | `185.199.108.153` | Proxied |
| **A** | `@` | `185.199.109.153` | Proxied |
| **A** | `@` | `185.199.110.153` | Proxied |
| **A** | `@` | `185.199.111.153` | Proxied |

*Note: In Cloudflare, `@` represents `rifaterdemsahin.com`.*

---

## 🔍 3. Records to VERIFY (No Change Needed)
These are already correct or dependent on the Apex record.

| Type | Name | Content | Status |
| :--- | :--- | :--- | :--- |
| **CNAME** | `hello` | `rifaterdemsahin.github.io` | **Correct**. Points to GitHub. |
| **CNAME** | `www` | `rifaterdemsahin.com` | **Correct**. Points to Apex (which you updated above). |

---

## ⚠️ 4. Records to LEAVE ALONE (Homelab & Email)
**Do not touch these**, or your homelab services and emails will stop working.

*   **Tunnels**: `chat`, `git`, `n8n`, `pgadmin`, `proxmox`, `rclone`, `router`, `sql`.
*   **Email**: `MX` records (`mx1.titan.email`, `mx2.titan.email`) and the `TXT` record (`v=spf1...`).

---

## 🚀 5. Post-DNS Steps
After updating Cloudflare:
1.  Go to your **GitHub Repository Settings** -> **Pages**.
2.  Ensure `rifaterdemsahin.com` is entered in the **Custom Domain** field.
3.  Wait for the **DNS Check** to pass (can take 5-30 minutes).
4.  Once green, check **Enforce HTTPS**.
