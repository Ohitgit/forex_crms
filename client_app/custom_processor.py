from client_app.models import *

def client_wallet(request):
    wallet_amount=None
    wallet_amounts=None
    if request.user.is_authenticated:
      try:

        
        wallet_amount=Client_Register.objects.get(user=request.user)
        wallet_amounts=wallet_amount.user_wallet
      except Client_Register.DoesNotExist:
         wallet_amount=None
         wallet_amounts=None
      return{'wallet_amounts':wallet_amounts}
    else:
        return {'wallet_amounts':wallet_amounts}

