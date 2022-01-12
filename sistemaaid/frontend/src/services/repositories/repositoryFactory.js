import AutorizacionRepository from "./autenticacion.repository";
import estudiosRepository from "./estudios.repository";
import ParticipantesRepository from "./participantes.repository";
import SedesRepository from "./sedes.repository";
import ColegiosRepository from "./colegios.repository";
import LugaresRepository from "./lugares.repository";
import CarrerasRepository from "./carreras.repository";
import ParticipanteCarrerasRepository from "./participante_carreras.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: estudiosRepository,
    Participantes: ParticipantesRepository,
    Sedes: SedesRepository,
    Carreras: CarrerasRepository,
    ParticipanteCarreras: ParticipanteCarrerasRepository,
    Colegios: ColegiosRepository,
    Lugares: LugaresRepository,
};

export default {
  get: (name) => repositories[name],
};