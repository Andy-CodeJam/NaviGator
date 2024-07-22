### Troubleshooting Log-In Issues with Spira

If a caller is having trouble logging into Spira and their password has not changed, it is likely due to a change in their LDAP (Lightweight Directory Access Protocol) entry. This can happen when network administrators reorganize departments in Active Directory (AD).

#### Quick Fix Steps:

1. **Check LDAP Entry**:
   - The issue often arises due to the user's department changing in LDAP (e.g., from OU=HQ to ,OU=LifePro).
   
2. **Update Required**:
   - The user's LDAP entry in Spira needs to be updated to reflect these changes.

3. **Report the Issue**:
   - Encouraging the user to report the issue in the support forum can expedite the resolution process.

#### Example Support Forum Post:

Here is a sample help forum post the user can use to report their issue:

```markdown
### Subject: Cannot Log into Spira

**Username:** [Your Username Here]

Hi Support Team,

I am unable to log into Spira. Although my password hasn't changed, I suspect it might be an issue with my LDAP entry as my department has recently been reorganized. 

Could you please update my LDAP entry in Spira?

Thank you,
[Your Name]
```

By directing the user to post in the support forum with this template, you can help ensure the issue is addressed quickly and effectively (see the article for a similar external example).

For further assistance, always encourage users to include their username and any pertinent details about recent changes to their organization structure ([source](#)).

By following these steps, the user should be able to regain access to Spira in a timely manner.