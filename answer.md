## Troubleshooting Spira Login Issues

### Common Reasons for Inability to Log On to Spira

If you or a user can't log on to Spira, there are a couple of common issues that could be the cause:

1. **LDAP/Active Directory Changes**: 
    - Often, trouble logging in can occur if the user's organization within LDAP has been changed. This is sometimes due to administrative changes like department reorganization in Active Directory. For example, moving from `OU=HQ` to `OU=LifePro` will require an update in Spira to reflect the new LDAP entry.
    - This is a quick fix. Please notify the support team with the username needing the update ([Article 1](#), [Article 3](#)).

2. **Access in UAT/QAT Environments**: 
    - If your issue specifically pertains to the QAT or UAT environments, note that these environments are periodically refreshed from production. Any users added to production in between these refreshes may not yet have accounts in QAT/UAT.
    - If you have production access but need access in QAT or UAT, you will need to request it ([Article 2](#)).

### Steps to Resolve

1. **Verify If It's an LDAP Issue**:
    - Confirm if there have been any recent updates to user departments or organizations in LDAP.
    - Notify the support team to update your LDAP entry by posting in the support forum with relevant details.

2. **Access Request for QAT/UAT**:
    - For access issues in QAT or UAT, post in the [Spira Support Channel](https://teams.microsoft.com/l/channel/19%3a8d7c611c16884bfeb4a952a427452251%40thread.skype/Support?groupId=f9fb4dcc-4bd7-4b02-be38-a325f73fe3e0&tenantId=0f087cc2-bc5d-40bf-8db4-41f99d0d1619).

### Sample Help Forum Post

To expedite the resolution, you can use the following template to post in the support forum:

```
@SupportTeam

I can't log into Spira.

**Username:** [Insert Username Here]
**Issue Description:**
- I am unable to log in despite having the correct username and password.
- I suspect there might have been a change in my department in LDAP.

**Additional Information:**
- Past department: [Insert Previous Department Here]
- Current department: [Insert Current Department Here]

Please assist with updating my LDAP entry in Spira.
```

This template includes the necessary details needed by the support team to address and resolve the LDAP-related login issue promptly.

By following these steps and providing the necessary information, you should be able to resolve login issues efficiently.