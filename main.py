from domain.Movie import Movie
from service.Catalog import Catalog

option = None

while option != 4 :

    try:
        print( 'Catalogo de películas' .center( 30, '-' ) )
        print( 'Menu \n  1. Agregar película\n  2. Listar películas\n  3. Eliminar archivo\n  4. Salir \n' )
        option = int( input( 'Escribe tu opción (1-4): ' ) )

        if option == 1 :
            movie_name = input( 'Nombre de la película: ' )
            movie = Movie( movie_name )
            Catalog .add( movie )

        elif option == 2 :
            Catalog .list()
        elif option == 3 :
            Catalog .delete()

    except Exception as e:
        print( f'Ocurrió un error\n  > { e }\n' )
        option = None

else :
    print( 'El programa a finalizado su ejecución' )