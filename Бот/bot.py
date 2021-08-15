from  aiogram  import  Bot , types
from  aiogram . dispatcher  import  Dispatcher
from  aiogram . utils  import  executor

from  config  import  TOKEN


bot  =  Bot ( token = TOKEN )
dp  =  Dispatcher ( bot )


@ Dp . message_handler ( commands = [ 'start' ])
async  def  process_start_command ( message : types . Message ):
    await  message . reply ( "Привіт! \ n Напиши мені що-небудь!" )


@ Dp . message_handler ( commands = [ 'help' ])
async  def  process_help_command ( message : types . Message ):
    await  message . reply ( "Напиши мені що-небудь, і я отпрпавлю цей текст тобі у відповідь!" )


@ Dp . message_handler ()
async  def  echo_message ( msg : types . Message ):
    await  bot . send_message ( msg . from_user . id , msg . text )


if  __name__  ==  '__main__' :
    executor . start_polling ( dp )   
