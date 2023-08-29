from visualizador.gs import gsapi


in_filename = r"C:\Users\everton.souza\Desktop\886905 Saco ENV448 Balanced Perro AD Natural Recipe Cerdo 15kg VG.pdf"
out_filename = r"C:\Users\everton.souza\Desktop\output_low_rgb.jpg"
params = ['gs',
          '-dNOPAUSE',
          '-dBATCH',
          '-sDEVICE=jpeg',
        #   '-r300',
          '-o', out_filename,
          '-f', in_filename
]

instance = gsapi.gsapi_new_instance(1)
gsapi.gsapi_init_with_args(instance, params)
