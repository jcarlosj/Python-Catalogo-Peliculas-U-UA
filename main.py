from domain.Movie import Movie
from service.Catalog import Catalog
import sys

def main() :

    option = None

    def add_movie() :
        movie_name = input( 'Nombre de la película: ' )
        movie = Movie( movie_name )
        Catalog .add( movie )

    def list_movies() :
        Catalog .list()

    def delete_file() :
        Catalog .delete()

    def exit() :
        return 4

    while option != 4 :

        try:
            print( 'Catalogo de películas' .center( 30, '-' ) )
            print( 'Menu \n  1. Agregar película\n  2. Listar películas\n  3. Eliminar archivo\n  4. Salir \n' )
            option = int( input( 'Escribe tu opción (1-4): ' ) )

            options = {
                1: add_movie,
                2: list_movies,
                3: delete_file,
                4: exit
            }

            # print( type( options ) )      # <class 'dict'>
            option = options[ option ]()

        except Exception as e:
            print( f'Ocurrió un error\n  > { e }\n' )
            option = None

    else :
        print( 'El programa a finalizado su ejecución' )

main()