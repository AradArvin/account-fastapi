from db.redis import check_otp


class OTPService:

    def __init__(self) -> None:
        pass


    async def get_user_id_if_verify(self, otp: str):
        user_id = await check_otp(otp)
        
        return user_id