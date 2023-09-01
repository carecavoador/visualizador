from visualizador.gs import gsapi


in_filename = r"C:\Users\everton.souza\Desktop\886912_V1_Anabe 2PK 10 LARGE ROLL BEEF ITEM 153 D08 12x39x4 (imported).pdf"
out_filename = r"C:\Users\everton.souza\Desktop\886912_V1_Anabe 2PK 10 LARGE ROLL BEEF ITEM 153 D08 12x39x4 (imported)_sop.jpg"

params = [
    'gs',
    '-dNOPAUSE',
    '-dBATCH',
    '-dOverprint=/simulate',
    '-sDEVICE=jpeg',
    '-r300',
    '-dTextAlphaBits=4',
    '-dGraphicsAlphaBits=4',
    '-o', out_filename,
    '-f', in_filename
]

instance = gsapi.gsapi_new_instance(1)
gsapi.gsapi_init_with_args(instance, params)
