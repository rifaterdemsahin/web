# Email Migration Guide: WordPress.com to Zoho Mail

This guide outlines the process for migrating the professional email service for `rifaterdemsahin.com` from WordPress.com (Titan/Professional Email) to Zoho Mail.

## 1. Objectives (1_Real)
- **Goal**: Zero data loss and minimal downtime during email provider transition.
- **Success Criteria**: 
  - All historical emails migrated to Zoho.
  - New emails received correctly in Zoho.
  - SPF/DKIM/DMARC configured for high deliverability.

## 2. Pre-Migration Checklist (2_Environment)
- [ ] **Current Provider Details**: Confirm your WordPress.com email password.
- [ ] **DNS Access**: Ensure you have access to your DNS provider (Cloudflare, as per recent migration).
- [ ] **Backup**: Although we will use IMAP migration, it is recommended to connect the current mailbox to a desktop client (Outlook or Thunderbird) and export a local backup (.pst or .mbox).

## 3. Implementation Steps (4_Formula)

### Phase 1: Setup Zoho Mail
1. **Sign up**: Go to [Zoho Mail](https://www.zoho.com/mail/) and choose your plan.
2. **Add Domain**: Add `rifaterdemsahin.com` to the Zoho Control Panel.
3. **Verify Ownership**: Zoho will provide a TXT record or CNAME record. Log in to **Cloudflare** and add this record to verify you own the domain.

### Phase 2: Configure DNS Records (Cloudflare)
Once verified, update the MX records in Cloudflare to point to Zoho. **Note: Remove the old WordPress.com/Titan MX records only after you are ready to start receiving mail at Zoho.**

**Zoho MX Records:**
| Host | Priority | Value |
| :--- | :--- | :--- |
| @ | 10 | mx.zoho.eu (or .com depending on your region) |
| @ | 20 | mx2.zoho.eu |
| @ | 50 | mx3.zoho.eu |

**SPF Record (TXT):**
Update your existing SPF record or create a new one:
`v=spf1 include:zoho.eu ~all`

**DKIM Record (TXT):**
Generate the DKIM selector in Zoho Control Panel and add the provided TXT record to Cloudflare.

### Phase 3: Data Migration (IMAP)
Zoho provides a built-in migration tool that is highly reliable.
1. In Zoho Mail Admin Console, go to **Data Migration**.
2. Select **IMAP** as the protocol.
3. **Server Details (WordPress.com/Titan)**:
   - IMAP Server: `imap.titan.email`
   - Port: `993`
   - SSL: `Yes`
4. **User Mapping**: Map your WordPress.com email address to the new Zoho mailbox.
5. **Start Migration**: Zoho will pull all folders and emails directly from the old server.

## 4. Validation (7_Testing)
- [ ] **Inbound Test**: Send an email from an external account (Gmail/Outlook) to `rifaterdemsahin.com`.
- [ ] **Outbound Test**: Send an email from Zoho to an external account.
- [ ] **Data Check**: Verify that all old folders and emails are visible in the Zoho interface.
- [ ] **DNS Check**: Use a tool like [MxToolbox](https://mxtoolbox.com/) to verify MX and SPF records.

## 5. Decommissioning
1. Once migration is 100% verified, go to your WordPress.com dashboard.
2. Disable "Auto-renew" for the "Professional Email" subscription.
3. Ensure you don't cancel until you are certain the data is safe in Zoho.
