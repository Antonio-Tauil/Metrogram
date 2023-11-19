from classes.user import User # Para usar la clase User
from utils.clear import clear # Para limpiar la consola
from unicodedata import normalize # Para eliminar tildes
from classes.post import Post # Para usar la clase Post


#DONE
def remove_accents(sting: str) -> str:
    '''
        Metodo que se encarga de eliminar los acentos de un string

        Args:
            string (str): String a eliminar acentos

        Returns:
            str: String sin acentos
    '''
    return normalize('NFKD', sting).encode('ASCII', 'ignore').decode('ASCII')

def search_user(user : User,users: [User], filter: str, department : bool) -> [User]:
    '''
        Metodo que se encarga de buscar un usuario por su username

        Args:
            users (list[User]): Lista de usuarios
            username (str): Username del usuario a buscar

        Returns:
            [User]: lista de usuarios encontrados
    '''
    results = []
    # Se limpia el string de caracteres especiales
    clean_filter = remove_accents(filter.lower())

    for _user in users:
        # Encuentra siempre y cuando el string que se pasa este contenido en el nombre de usuario o en la carrera ignorando los caracteres especiales
        if department and clean_filter in remove_accents(_user.get_career().lower()) and _user.get_user_id() != user.get_user_id():
            results.append(_user)
        elif clean_filter in remove_accents(_user.get_username().lower()) and _user.get_user_id() != user.get_user_id():
            results.append(_user)

    return results 
    
def select_profile(current_user: User, show: bool, results : [User], is_to_follow):
    '''
        Metodo que se encarga de seleccionar los perfiles de los usuarios encontrados

        Args:
            show (bool): Si se muestran o no los perfiles
            results (list[User]): Lista de usuarios encontrados

        Returns:
            None
    '''
    if not show:
        return
    
    # opcion de ver el perfil de alguno de los usuarios encontrados basado en indice
    op = input(f"\t\tIngrese el numero de perfil que desea {'seguir' if is_to_follow else 'ver'}: ")
    while not op.isdigit() or int(op) > len(results) or int(op) < 1:
        print("\t\tOpcion invalida")
        op = input(f"\t\tIngrese el numero de perfil que desea {'seguir' if is_to_follow else 'ver'}: ")

    clear()
    profile : User = results[int(op)-1]
    if is_to_follow: # si estoy en el menu de gestion de interacciones es para seguir al usuario
        """"""
        # a profile le tengo que agregar en follow requests currrent_user
        # Si las carreras son las mismas en vez de agregar a los follow request de profile se hace un follow desde user hasta profile
        already_follows = any(following.get_user_id() == profile.get_user_id() for following in current_user.get_following())

        already_has_follow_request = any(follow_request.get_user_id() == current_user.get_user_id() for follow_request in profile.get_follow_requests())


        if not already_follows:
            if not already_has_follow_request:
                # Si estudian la misma carrera el follow es automatico
                if remove_accents(profile.get_career().lower()) == remove_accents(current_user.get_career().lower()):
                    current_user.follow_user(profile)
                    print(f"\t\tAhora sigues a {profile.get_username()}")
                else:
                    profile.register_follow_request(current_user)
                    print(f"\t\tSe ha enviado la solicitud de seguimiento a {profile.get_username()}")
            else:
                print(f"\t\tYa mandaste la solicitud de seguimiento a {profile.get_username()}")
        else:
            print(f"\t\tYa sigues a {profile.get_username()}")

        input("\t\tPresione enter para continuar")
        clear()

    else: # Si estoy en el menu de gestion de perfil 
        # se verifica si el usuario actual puede ver el perfil del usuario seleccionado (Si current_user sigue al usuario seleccionado)
        if (profile not in current_user.get_following()):
            print("\t\tNo puedes ver este perfil, ya que no lo sigues!")
            input("\t\tPresione enter para continuar...")
            clear()
            return
        
        print(f"\t\t{profile.get_name()} {profile.get_username()}")
        for idx,post in enumerate(profile.get_posts()):
            print(f"\t\t{idx+1}.- {post.get_caption()[:50]+'...' if len(post.get_caption()) > 50 else post.get_caption()}")
        
        view_post = input("\t\tDesea ver alguno de los posts? (s/n)")
        while view_post not in ["s","n", "S", "N"]:
            print("\t\tOpcion invalida")
            view_post = input("\t\tDesea ver alguno de los posts? (s/n)")

        show_post(view_post in ["s","S"], profile.get_posts())

def show_post(view_post : bool, _posts : [Post]):
    '''
        Metodo que se encarga de mostrar los posts de un usuario

        Args:
            view_post (bool): Si se quiere mostrar o no
            _posts (list[Post]): Lista de posts

        Returns:
            None
    '''
    if not view_post:
        return
    
    op = input("\t\tIngrese el numero de post que desea ver: ")
    while not op.isdigit() or int(op) > len(_posts) or int(op) < 1:
        print("\t\tOpcion invalida")
        op = input("\t\tIngrese el numero de post que desea ver: ")

    clear()
    post = _posts[int(op)-1]
    print(f"\t\t{post.get_caption()}")
    print(f"\t\t{post.get_multimedia()}")
    print(f"\t\t{post.get_date()}")
    print("\n\t\tInteracciones\n")
    post.print_interactions()
    input("\t\tPresione enter para continuar...")
    clear()

def search_profile_menu(user : User, users: [User], is_interaction_menu: bool):
    
    op = "-1"

    while op != "0":
        print("\t\tBúsqueda de perfiles\n")
        print("\t\t1.- Buscar por usuario")
        print("\t\t2.- Buscar por carrera o departamento")
        print("\t\t0.- Salir")
        op = input("\t\tIngrese una opcion: ")

        # Dependiendo de lo que elija el usuario, se filtra por username o por carrera/dep
        if op == "1":
            if results:= search_user(user, users, input("\t\tIngrese el nombre de usuario: "), department=False):
                print()
                for idx,result in enumerate(results):
                    print(f"\t\t{idx+1}.-{result.get_username()} - {result.get_career()}")

                if is_interaction_menu:
                    select_profile(user, True, results, is_interaction_menu)
                else:
                    # posibilidad de ver el perfil de alguno de los usuarios encontrados
                    view_profile = input("\t\tDesea ver el perfil de alguno de estos usuarios? (s/n)")
                    while view_profile not in ["s","n", "S", "N"]:
                        print("\t\tOpcion invalida")
                        view_profile = input("\t\tDesea ver el perfil de alguno de estos usuarios? (s/n)")
                    select_profile(user, view_profile in ["s","S"], results, is_interaction_menu)
            else:
                print("\n\t\tNo se encontraron resultados")
                input("\t\tPresione enter para continuar...")
        
        elif op == "2":
            if results := search_user(user, users,input("\t\tIngrese la carrera o departamento: "),department=True,):
                print()
                for idx,result in enumerate(results):
                    print(f"\t\t{idx+1}.-{result.get_username()} - {result.get_career()}")
                if is_interaction_menu:
                    select_profile(user, True, results, is_interaction_menu)
                else:
                # posibilidad de ver el perfil de alguno de los usuarios encontrados
                    view_profile = input("\t\tDesea ver el perfil de alguno de estos usuarios? (s/n)")
                    while view_profile not in ["s","n", "S", "N"]:
                        print("\t\tOpcion invalida")
                        view_profile = input("\t\tDesea ver el perfil de alguno de estos usuarios? (s/n)")
                    select_profile(user, view_profile in ["s","S"], results, is_interaction_menu)
            else:
                print("\t\tNo se encontraron resultados")
                input("\t\tPresione enter para continuar...")

        elif op == "0":
            clear()
            return

        else:
            print("\t\tOpcion invalida")
            input("\t\tPresione enter para continuar...")
        clear()

    clear()