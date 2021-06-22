import pathlib, os

class Catalog :

    file_name = 'movies.txt'
    path = pathlib .Path( __file__ ) .parent .absolute()

    @classmethod
    def add( cls, movie ) :
        with open( f'{ str( cls .path ) }/{ cls .file_name }', 'a', encoding='utf8' ) as file :
            file .write( f'{ movie }\n' )

    @classmethod
    def list( cls ) :
        with open( f'{ str( cls .path ) }/{ cls .file_name }', 'r', encoding='utf8' ) as file :
            print( 'Catálogo de películas' .center( 50, '-' ) )
            print( file .read() )

    @classmethod
    def delete( cls ) :
        os .remove( f'{ str( cls .path ) }/{ cls .file_name }' )
        print( f'El archivo { cls .file_name } ha sido eliminado' )
