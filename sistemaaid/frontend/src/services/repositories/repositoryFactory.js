import AutorizacionRepository from "./autenticacion.repository";
import EstudiosRepository from "./Estudios/estudios.repository";
import EdicionesRepository from "./Estudios/ediciones.repository";
import MuestraPonderadaRepository from "./Estudios/muestraPonderada.repository";
import MetodologiaRepository from "./Estudios/metodologia.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: EstudiosRepository,
    Ediciones: EdicionesRepository,
    MuestraPonderada: MuestraPonderadaRepository,
    Metodologia:MetodologiaRepository
};

export default {
  get: (name) => repositories[name],
};