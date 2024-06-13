import numpy as np
import pyqcm
import os
import sys
from new_model_2x2_2C_8b_C2v_L import model
from new_cluster_2x2_2C_8b_C2v_L import CM
import pyqcm.cdmft as cdmft
from Information_mat import *


param = "mu"
current_file_dir = os.path.dirname(os.path.abspath(__file__))
mat = Dic_mat[Clé_mat]
# path = f'{current_file_dir}/new_{Phase}/{mat}/fades/fade_{mat}_final_mu_{mat_mu}_U={Valeur_U}.tsv'
path = f"/net/nfs-iq/data/lbsc/Maîtrise_LBSC/Révision_stage_2022/new_supra/Bi2Sr2Ca2Cu3O10_inner/données/données_boucle_mu_Bi2Sr2Ca2Cu3O10_inner_U=13.8.tsv"
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(path)

data = np.genfromtxt(path, names=True)
param_dep = data[param][-1]#Valeur de départ de la boucle
Valeur_U = data["U"][-1]
param_fin = float(13) #Valeur du paramètre de boucle que l'on veut atteindre
# param_fin = float(sys.argv[1])


non_variable_parameters = ["U",
    "mu",
    "D",
    "e",
    "tpp",
    "tppp",
    "tpd"
]
variable_parameters = [
    "sb1_1",
    "sb2_1",
    "sb3_1",
    "sb4_1",
    "sb5_1",
    "sb6_1",
    "sb7_1",
    "sb8_1",
    "eb1_1",
    "eb2_1",
    "eb3_1",
    "eb4_1",
    "eb5_1",
    "eb6_1",
    "eb7_1",
    "eb8_1",
    "tb1_1",
    "tb2_1",
    "tb3_1",
    "tb4_1",
    "tb5_1",
    "tb6_1",
    "tb7_1",
    "tb8_1"
]


if Phase =="normale":
    target_sectors = ["R0:N12:S0/R0:N10:S0/R0:N14:S0","R0:N8:S0"]
    non_variable_parameters.remove("D")
    variable_parameters.remove("sb1_1")
    variable_parameters.remove("sb2_1")
    variable_parameters.remove("sb3_1")
    variable_parameters.remove("sb4_1")
    variable_parameters.remove("sb5_1")
    variable_parameters.remove("sb6_1")
    variable_parameters.remove("sb7_1")
    variable_parameters.remove("sb8_1")
if Phase =="supra":
    target_sectors = ["R0:S0","R0:N8:S0"]
parameter_names = non_variable_parameters+variable_parameters


parametres = """
"""
for name in parameter_names:
    parametres += '\n'+name+'='+str(data[name][-1])


model.set_target_sectors(target_sectors)
model.set_parameters(parametres)


# #cdmft

isExist = os.path.exists(f"{current_file_dir}/new_{Phase}/{mat}/données")
if isExist == False:
    os.makedirs(f"{current_file_dir}/new_{Phase}/{mat}/données")
os.chdir(f"{current_file_dir}/new_{Phase}/{mat}/données")
if Phase == "normale":
    filename = f'données_boucle_{param}_U={Valeur_U}_n.tsv'
if Phase == "supra":
    filename = f'données_boucle_{param}_{mat}_U={Valeur_U}_n.tsv'
def run_cdmft():
    solution=cdmft.CDMFT(model,variable_parameters, accur=1e-3, accur_dist=1e-8, method='Nelder-Mead', file = filename, maxiter = 100, convergence=['self-energy'])
    return solution.I

if param_dep > param_fin:
    step = -0.01
if param_dep < param_fin:
    step = 0.01
#Boucle sur le potentiel chimique
model.controlled_loop(task=run_cdmft, varia=variable_parameters, loop_param=param, loop_range=((param_dep,param_fin,step)))