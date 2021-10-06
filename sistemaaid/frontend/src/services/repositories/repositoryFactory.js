import AutorizacionRepository from "./autenticacion.repository";
import EstudiosRepository from "./Estudios/estudios.repository";
import EdicionesRepository from "./Estudios/ediciones.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: EstudiosRepository,
    Ediciones: EdicionesRepository,
};

export default {
  get: (name) => repositories[name],
};