ROL = {
  0: 'Urologo',
  1: 'Enfermero',
  2: 'Paciente'
}

EXITUSSTATE = {
  0 : 'No',
  1 : 'Sí',
}
PROGRESIVASTATE = {
  0 : 'No',
  1 : 'Menores características',
  2 : 'Iguales características',
  3 : 'Mayores características',
}

RECIDIVASTATE = {
  0:'No',
  1 : 'Estadio (T)',
  2 : 'Ganglios (N)',
  3 : 'Metástasis (M)',
}

EVOLDESFAVORABLESTATE = {
  0 : 'No',
  1 : 'Sí',
}

# USERS MESSAGES #
USER_EXIST = 'El usuario ya se encuentra registrado'
USER_REGISTER_OK = 'Usuario registrado correctamente'
DNI_NOT_FOUND = 'DNI no encontrado'
REGISTER_OK = 'Usuario registraado con suceso.'
USER_NOT_FOUND = 'Usuario no encontrado'
NO_USERS = 'No hay usuarios registrados'
USER_DELETED = 'Usuario eliminado correctamente'
USER_UPDATED = 'Datos del usuario actualizados correctamente'

#PATIENTS MESSAGE#
HC_REGISTER_OK = 'História Clínica registrada correctamente'
INVALID_PATIENTID = "Introduce un identificador válido para el paciente"
PATIENT_NOT_FOUND = 'Paciente no encontrado'
NO_PATIENTS = 'No hay pacientes registrados.'
SET_OF_HC = 'Se ha dado la baja al paciente correctamente'

#MODELS TRAINING MESSAGES#
NOT_VALID_METHOD = 'Elige un método válido'
KNN_TRAINED = 'El modelo ha sido reentrenado con el metodo K-NN'
RANDOM_FOREST_TRAINED = 'El modelo ha sido reetrenado con el método Randon Forest'
KMEANS_TRAINED = 'El modelo ha sido reetrenado con el método KMeans'
NAIVE_BAYES_TRAINED = 'El modelo ha sido reetrenado con el método Naive Bayes'


#MODELS ROUTES#
KMEANS_MODEL_ROUTE = 'IA_Models/kmeans.pkl'
KNN_MODEL_ROUTE = 'IA_Models/knn_model.pkl'
RANDOM_FOREST_MODEL_ROUTE = 'IA_Models/random_forest_model.pkl'
NAIVE_BAYES_MODEL = 'IA_Models/naive_bayes_model.pkl'


#PARAMETROS
INVALID_PARAMETER = 'El parámetro debe ser un número entero mayor que cero'