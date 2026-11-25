import snowflake.connector
import getpass

USER = "SDPOLLACK"
ACCOUNT = "UGYOIFL-LO18790"
PASSWORD = "DeMeals@DEA2026!"
AUTH = input("Enter MFA code: ")

try:
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        authenticator="USERNAME_PASSWORD_MFA",
        passcode=AUTH
    )

    # print("Successfully connected to Snowflake!")

except Exception as e:
    print("Connection failed:", e)