import AutorizacionRepository from "./autenticacion.repository";

const repositories = {
    Autorizacion: AutorizacionRepository
};

export default {
  get: (name) => repositories[name],
};