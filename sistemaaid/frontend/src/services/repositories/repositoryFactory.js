import AutorizacionRepository from "./autenticacion.repository";
import estudiosRepository from "./estudios.repository";
import ParticipantesRepository from "./participantes.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: estudiosRepository,
    Participantes: ParticipantesRepository,
};

export default {
  get: (name) => repositories[name],
};