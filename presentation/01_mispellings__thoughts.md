**Thinking:** `[Is the user asking about Spira?]`

**Thinking:** `[Y]`

**Thinking:** `[Is the user asking about a single topic, multiple topics, or no topics?]`

**Thinking:** `[S]`

**Thinking:** `[The user is asking about a single topic. I can proceed.]`

**Thinking:** `[Someday I will rephrase the prompt and pass it to Azure AI Search, but for now I will just return the original prompt.]`

**Thinking:** `[Original prompt: Why I no abel to looge oohn too speerya?]`

**Thinking:** `[Rephrased prompt: Why I no abel to looge oohn too speerya?]`

**Thinking:** `[I have the top articles from the original knowledge base and from the Spira documentation, as returned by Azure AI search.]`

**Thinking:** `[I will check each one individually to decide whether or not it is likely to be among the top 3 most useful articles for the user prompt.]`

**Thinking:** `[This will make it easier to generate a response to the user's query.]`

**Thinking:** `[Checking QA KB article 1 for usefulness.]`

**Thinking:** `[QA KB article 1 is likely to be useful, so I will keep it:`
```
{'question': "My password hasn't changed but I can't log in to Spira", 'answer': "We have had a few users who have had trouble logging in recently, even though the users have accounts and have logged in before.\\n\\nAny that we have run into have been a matter of the users have changed departments in LDAP. The user isn't doing anything differently, it seems like Network Admin is cleaning up/separating departments in Active Directory. For example a users organization is changing from OU=HQ to ,OU=LifePro - This means that we have to update your LDAP entry in Spira. This is a quick fix, we just need to know about it.\\n\\nIf you want it done quickly, post to the support Forum @Gardner, Robyn - I can't log into Spira and include your username. We'll get you back quickly once we know it's a problem."}
```

**Thinking:** `[Checking QA KB article 2 for usefulness.]`

**Thinking:** `[QA KB article 2 is likely to be useful, so I will keep it:`

```
{'question': "Why can't I log in anymore?", 'answer': "We have had a few users who have had trouble logging in recently, even though the users have accounts and have logged in before.\\n\\nAny that we have run into have been a matter of the users have changed departments in LDAP. The user isn't doing anything differently, it seems like Network Admin is cleaning up/separating departments in Active Directory. For example a users organization is changing from OU=HQ to ,OU=LifePro - This means that we have to update your LDAP entry in Spira. This is a quick fix, we just need to know about it.\\n\\nIf you want it done quickly, post to the support Forum @Gardner, Robyn - I can't log into Spira and include your username. We'll get you back quickly once we know it's a problem."}
```

**Thinking:** `[Checking QA KB article 3 for usefulness.]`

**Thinking:** `[QA KB article 3 is not likely to be useful, so I will discard it:`

```
{'question': 'List value blank', 'answer': 'Custom properties can be populated with a list of custom values (as opposed to a single date, boolean, or text value). A value in the list can be deactivated without deactivating the entire list itself. If this happens, the deactivated value will no longer display in the detail view of the affected artifacts. The value will continue to display in the list view.\\n\\nFor an illustration of the issue, see [this post](https://teams.microsoft.com/l/message/19:8d7c611c16884bfeb4a952a427452251@thread.skype/1667473265479?tenantId=0f087cc2-bc5d-40bf-8db4-41f99d0d1619&groupId=f9fb4dcc-4bd7-4b02-be38-a325f73fe3e0&parentMessageId=1667473265479&teamName=Spira%20Training%20and%20Support&channelName=Support&createdTime=1667473265479&allowXTenantAccess=false) from the Spira Support channel.'}
```

**Thinking:** `[Checking Docs article 1 for usefulness.]`

**Thinking:** `[Docs article 1 is not likely to be useful, so I will discard it:`

```
{'title': 'SpiraCapture', 'content': 'ion 6.1+ You will not be able to create an incident in Spira if your product or workflow is set up such that a custom field cannot be left blank and it was not filled out within the form. Some custom properties may have limitations on them such as maximum or minimum values which SpiraCapture cannot enforce directly. These will also block incident creation, but an error message should be displayed which explains where the issue is and why it occurred to provide an opportunity to fix it and try again.', 'entity': 'PRODUCT', 'value': 'SpiraCapture | Spira | SpiraCaptures', 'url': 'https://spiradoc.inflectra.com/About/introduction-to-spira/../../SpiraCapture/User-Guide/'}
```

**Thinking:** `[Checking Docs article 2 for usefulness.]`

**Thinking:** `[Docs article 2 is not likely to be useful, so I will discard it:`

```
{'title': 'System', 'content': 'you choose to enter it, the user\'s name should be the fully-distinguished name of the user (e.g. CN=Sample User, CN=Users, OU=Headquarters, DC=MyCompany, DC=Com).  Security Settings┬╢ The "Security Settings" administration page lets you specify the various security settings within SpiraPlan to match your organization\'s policies and processes:   The following settings can be changed within the system, once you are satisfied, click the "Save" button to commit the changes:  Allow User Registration: Set this to "Yes" if you want to allow users to self-register for SpiraPlan accounts (that you can subsequently approve). If you set this to "No", a system administrator will need to create all user accounts. Also set this to "No" if you plan on using LDAP-based authentication. HTTPS Only: Set this to Yes if the application will only be running on HTTPS. This enables tighter security that is only available on HTTPS. Minimum Required Password Length: Set this to the minimum length of passwords in the system. Choosing a longer password will make it harder for an unauthorized user to crack a password and gain entry into the system. Minimum Required Special Characters - Set this to the minimum number of non-alphanumeric characters that will be required for passwords in the system. Choosing more required special characters will make it harder for an unauthorized user to crack a password and gain entry into the system. Maximum # Invalid Password Attempts: Set this to the number of times a user can enter an incorrect password (during the time window specified in the setting below) before their account is temporarily locked out. This is important in preventing \'brute force\' password hacking attempts. Max Login Attempts Window: Set this to the number of minutes over which invalid login attempts are evaluated before locking the user\'s account. Account Lockout Period: Set this to the duration (in minutes) to keep an account locked after too many invalid login attempts. Password Change I', 'entity': 'PRODUCT', 'value': 'SpiraApp | GitLab | Standard edition | Subversion | BitBucket | SpiraTest | Windows ActiveDirectory | TaraVault | Azure DevOps | SpiraPlan┬« | SpiraApps | SCM | SpiraPlan | Git | Integration | Inflectra | the FMEA SpiraApp | Instant Messenger | Spira | SpiraTeam | Version Control Integration | SQL Server | Trial', 'url': 'https://spiradoc.inflectra.com/About/introduction-to-spira/../../Spira-Administration-Guide/System/'}
```

]

**Thinking:** `[Checking Docs article 3 for usefulness.]`

**Thinking:** `[Docs article 3 is not likely to be `useful, so I will discard it:

{'title': 'Product Management', 'content': "Introduction to Spira┬╢ The SpiraΓäó family of applications from Inflectra┬« are a powerful set of tools that help you manage your software lifecycle. SpiraTest┬« is our powerful and easy to use requirements, test and defect management system, ideal for quality assurance teams. SpiraTeam┬« is our integrated Application Lifecycle Management (ALM) system that manages your product's requirements, releases, test cases, issues, tasks, and risks in one unified environment. SpiraPlan┬« expands on the features in SpiraTeam┬« to provide a complete Enterprise Agile Planning┬« solution that lets you manage products, programs and the entire organization with ease. Quality Assurance┬╢ Quality Assurance is a key component of the Software Development Life-Cycle (SDLC), which needs to be integrated into the planning and management of a program or product from its inception. Too often though, QA is implemented as Quality Control - whereby testing that the required functionality works as expected, is performed at the end, when it is most costly to make corrections and changes. To manage QA across a product from day one, it is imperative that the original requirements are documented together with the use-cases that validate the desired functionality. These use-cases then form the basis of the test scripts that can be executed to validate that the functionality has been correctly built, and that the requirements have been satisfied. During the execution of these test scripts, failures may occur, which are recorded as incidents - either to be fixed or documented depending on the severity. Typically, these activities require people to use at least three different types of software:  Requirements Management Test Script Management Defect / Issue / Bug Tracking  However, this stove-piped approach has many limitations and drawbacks, most importantly the fact that there is no traceability between the different artifacts. How can the product manager know that all the requirements have been tested? Conve", 'entity': 'ORG', 'value': 'Inflectra', 'url': 'https://spiradoc.inflectra.com/About/introduction-to-spira/#quality-assurance'}

]

**Thinking:** `[I have evaluated all the articles.]`

**Thinking:** `[I started with 3 QA KB articles and now `have 2 useful ones.]

**Thinking:** `[I started with 3 Docs articles and now `have 0 useful ones.]

**Thinking:** `[Now that I have useful articles, I will `use them to generate a response to the user's query.]

**Thinking:** `[I have generated a response.]`

**Thinking:** `[Here is my response:]`

**Thinking:** `[# Troubleshooting Login Issues for Spira`

If a user is unable to log into Spira, there are a few common issues that could be the cause:

## Common Causes and Solutions

1. **LDAP Department Changes**:
    - Recently, we have seen login issues when users change departments in LDAP (Active Directory). The user might not have done anything differently, but network admins may have reorganized departments.
    - Example: If a userΓÇÖs organization changes from `OU=HQ` to `OU=LifePro`, we need to update their LDAP entry in Spira.
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
- [Why users canΓÇÖt log in anymore](#)]

**Thinking:** `[I need to evaluate whether or not the `question was answered?]

**Thinking:** `[Y]`

**Thinking:** `[The question was answered by the `proposed draft response. I will return the response to the user.]

