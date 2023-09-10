from visualizador.gs import gsapi


in_filename = r"C:\Users\everton.souza\Desktop\872670_V2 166694 Anabe_5 Small Rolls_D08_12x29 5_4 sanfona__.pdf"
out_filename = r"C:\Users\everton.souza\Desktop\872670_V2 166694 Anabe_5 Small Rolls_D08_12x29 5_4 sanfona__.tif"

params = [
    'gs',
    '-dNOPAUSE',
    '-dBATCH',
    # '-dOverprint=/simulate',
    '-sDEVICE=tiffsep',
    '-r600',
    '-dTextAlphaBits=4',
    '-dGraphicsAlphaBits=4',
    '-o', out_filename,
    '-f', in_filename
]

instance = gsapi.gsapi_new_instance(1)
gsapi.gsapi_init_with_args(instance, params)
