from data.fetch_data import fetch_data
from menus.modules_menu.modules_menu import modules_menu
from utils.util import save_data
from auth.login import login
from auth.register import register
from utils.clear import clear
from utils.util import read_from_txt

def main_menu():
    '''
        Metodo que se encarga de mostrar el menu principal
    '''
    clear()
    current_user = None
    # Realiza una validacion para ver si ya se tienen los datos o hay que pedirlos al API
    # Si no existe el Txt entonces lee del API, sino del Txt
    users, posts, deleted_users, deleted_posts = read_from_txt()  if read_from_txt() is not None else fetch_data()

    if (users is None or posts is None):
        print("No se pudo cargar la informacion")
        return

    save_data(users, posts, deleted_users, deleted_posts)

    op = "-1"
    while op != '0':
        print("\t\tMetrogram\n")
        print("\t\t1. Ingresar")
        print("\t\t2. Registrarse")
        print("\t\t0. Salir")
        op = input("\t\tIngrese una opcion: ")

        if op == '1':
            if current_user := login(users):
                modules_menu(current_user, users, posts,deleted_users ,deleted_posts,)

        elif op == '2':
            if current_user := register(users):
                modules_menu(current_user, users, posts,deleted_users ,deleted_posts,)

        elif op == '0':
            print("\t\tGracias por usar Metrogram")
            break
        
        else: 
            print("\t\tOpcion invalida...")
            input("\t\tPresione enter para continuar")
            clear()
    
    save_data(users, posts, deleted_users, deleted_posts)



    
