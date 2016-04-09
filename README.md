# fitbit-python
After authorizing and receiving access token with OAuth 2.0 maintain python app connection using the refresh token. A use case for this would be providing a script access to your personal fitbit data to perform some action. As an example I have used an iteration of this to turn off my samsung tv once sleep data was logged. (However this did take additional efforts to continously sync data to fitbit's servers)

#Prerequisites 
Requires creating an account and new application from https://dev.fitbit.com

Initially requires pre-authorizing an application, obtaining and providing the authorization, access, and refresh tokens. This can be done through:
- Code
- fitbits API Debugger https://dev.fitbit.com/apps/oauthtutorialpage. 
- A REST Debugger Tool like Postman
- Temboo - simplified API tools https://temboo.com (Preffered method due to ease)

#Steps to Obtain Tokens (Temboo.com)
1. Create a Temboo account
2. With your Temboo account create a new application at dev.fitbit.com being sure to set the "Callback URL" to https://{Your Temboo Account Name}.temboolive.com/callback/fitbit
3. Goto https://temboo.com/library/Library/Fitbit/OAuth/InitializeOAuth/ and insert your Client ID and Scope (see https://dev.fitbit.com/docs/oauth2/#scope for scope types)
4. Click Run and Follow the temboo's steps to access the URL to authorize your app through fitbit.
5. You will recieve your authorization token enter that in refresh.py
6. Copy the access token in a file named access.txt and provide the path to refresh.py
7. Copy the refresh token in a file named refresh.txt and provide the path to refresh.py
