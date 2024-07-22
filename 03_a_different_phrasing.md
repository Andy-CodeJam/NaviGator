## Troubleshooting Login Issues with Spira

When customers report issues logging into Spira, it is essential to consider common scenarios and possible fixes:

### Scenario 1: LDAP Changes
If the user's department or organizational unit (OU) has changed recently in LDAP, this might affect their login credentials. Network administrators may reorganize departments, causing a mismatch in user information stored on the server.

#### Solution
To resolve this, update the user's LDAP entry in Spira. This is a quick fix once the issue is identified.

**Sample Support Forum Post:**
```
@Gardner, Robyn - I can't log into Spira
Username: [User's Username]
```
Please include the username and note the recent organizational changes for a speedy resolution. For more details, refer to the relevant article [here](#question-my-password-hasnt-changed-but-i-cant-log-in-to-spira).

### Scenario 2: Access in UAT Environment
If the issue pertains to accessing Spira in the User Acceptance Testing (UAT) environment, it could be due to periodic refreshes from the production environment. User access and permissions are updated during these refreshes, possibly excluding users added after the last refresh.

#### Solution
Users who need consistent access to QAT or UAT should ensure their details are in the production environment. If access is still needed, they can request it through the designated Support Channel.

**Sample Support Forum Post:**
```
Subject: Access Request for Spira UAT

Hi Team,

I have production access to Spira but cannot access the UAT environment. Could you please help grant access?

Name: [Your Name]
Username: [Your Username]
Department: [Your Department]

Thank you,
[Your Contact Information]
```
Direct users to the [Spira Support Channel](https://teams.microsoft.com/l/channel/19%3a8d7c611c16884bfeb4a952a427452251%40thread.skype/Support?groupId=f9fb4dcc-4bd7-4b02-be38-a325f73fe3e0&tenantId=0f087cc2-bc5d-40bf-8db4-41f99d0d1619) for this issue.

For more details on this scenario, please visit the relevant article [here](#i-cant-access-spira-in-uat).

By following these guidelines, you can quickly troubleshoot login issues and provide efficient support to users experiencing problems with Spira.