## Troubleshooting Login Issues in Spira

### Issue Description
If a user is unable to log into Spira despite having an established account and a known password, it is likely due to changes in their department structure within LDAP (Active Directory). This commonly happens when network administrators reorganize user groups or departments.

### Common Cause
This problem typically occurs because the user's organization structure in LDAP has been updated. For instance, moving from `OU=HQ` to `OU=LifePro`. When this happens, the user's LDAP entry in Spira must be updated to reflect these changes ([Article 1](#), [Article 2](#)).

### Quick Fix
To resolve this quickly, you need to inform the Spira support team about the issue. You can post a message in the support forum with the necessary details.

### Sample Help Forum Post

```
@SupportTeam - I can't log into Spira

- Username: [Your Username Here]
- Issue Description: Unable to log in after department change in LDAP
- Former Department: [Old Department (e.g., OU=HQ)]
- New Department: [New Department (e.g., OU=LifePro)]

Please update my LDAP entry in Spira to reflect the new department.
```

Using the above template, fill in the specific details and post it in the Support Forum to expedite the resolution process.

Feel free to get in touch with any further questions, and we’ll assist you promptly.

### Note to the Support Representative
Ensure you get the username and department details from the caller to assist in crafting a precise forum post. This will speed up the resolution process significantly.

---
*Articles Referenced:*
- [Cause: LDAP Department Changes](#)
- [Resolution: Informing Spira Support](#)

---

For more details, please refer to the documentation or contact the support team if you encounter further issues.