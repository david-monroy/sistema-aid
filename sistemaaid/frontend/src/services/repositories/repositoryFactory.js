import AutorizacionRepository from "./autenticacion.repository";
import EstudiosRepository from "./Estudios/estudios.repository";
import EdicionesRepository from "./Estudios/ediciones.repository";
import MuestraPonderadaRepository from "./Estudios/muestraPonderada.repository";
import ParticipantesRepository from "./participantes.repository";
import SedesRepository from "./sedes.repository";
import ColegiosRepository from "./colegios.repository";
import LugaresRepository from "./lugares.repository";
import CarrerasRepository from "./carreras.repository";
import ParticipanteCarrerasRepository from "./participante_carreras.repository";
import MetodologiaRepository from "./Estudios/metodologia.repository";
import ListaCodigoRepository from "./Estudios/listaCodigo.repository";

const repositories = {
    Autorizacion: AutorizacionRepository,
    Estudios: EstudiosRepository,
    Ediciones: EdicionesRepository,
    MuestraPonderada: MuestraPonderadaRepository,
    Metodologia:MetodologiaRepository,
    ListaCodigo: ListaCodigoRepository,
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