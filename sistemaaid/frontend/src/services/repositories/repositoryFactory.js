import AutorizacionRepository from "./autorizacion.repository";

const repositories = {
    Autorizacion: AutorizacionRepository
};

export default {
  get: (name) => repositories[name],
};