import AutorizacionRepository from "./autenticacion.repository";
import estudiosRepository from "./estudios.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: estudiosRepository,
};

export default {
  get: (name) => repositories[name],
};