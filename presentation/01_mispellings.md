# Troubleshooting Login Issues for Spira

If a user is unable to log into Spira, there are a few common issues that could be the cause:

## Common Causes and Solutions

1. **LDAP Department Changes**:
    - Recently, we have seen login issues when users change departments in LDAP (Active Directory). The user might not have done anything differently, but network admins may have reorganized departments.
    - Example: If a user’s organization changes from `OU=HQ` to `OU=LifePro`, we need to update their LDAP entry in Spira.
    - **Solution**: This is a quick fix, but we need to be informed about the change.
    - Reference: [FAQ on password issues not due to changes](#) and [FAQ on users unable to log in](#).

## Sample Help Forum Post

To expedite the resolution, you can post to the support forum with the following information:

```markdown
**Post Title**: Can't log into Spira

**Post Content**:
Hi Support Team,

My login credentials have not changed but I am unable to access Spira. I suspect it might be due to a recent change in my department in LDAP. Here are my details:

- **Username**: [Your Username]
- **Previous Department**: [OU=HQ]
- **Current Department**: [OU=LifePro]

Please update my LDAP entry in Spira as per the change. Thank you!

Best regards,  
[Your Full Name]
```

Encourage the user to provide accurate details to ensure a swift resolution.

Happy Troubleshooting!

**Note**: Ensure all placeholders are appropriately filled with the user's details before posting.

---

Cited from:
- [Question about unchanged passwords](#)
- [Why users can’t log in anymore](#)