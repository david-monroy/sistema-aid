import AutorizacionRepository from "./autenticacion.repository";
import EstudiosRepository from "./Estudios/estudios.repository";
import EdicionesRepository from "./Estudios/ediciones.repository";
import MuestraPonderadaRepository from "./Estudios/muestraPonderada.repository";
import ParticipantesRepository from "./Participantes/participantes.repository";
import SedesRepository from "./Comun/sedes.repository";
import ColegiosRepository from "./Comun/colegios.repository";
import LugaresRepository from "./Comun/lugares.repository";
import CarrerasRepository from "./Comun/carreras.repository";
import ParticipanteCarrerasRepository from "./Participantes/participante_carreras.repository";
import MetodologiaRepository from "./Estudios/metodologia.repository";
import UsuariosRepository from "./usuarios.repository";
import ListaCodigoRepository from "./Estudios/listaCodigo.repository";
import PreguntasRepository from "./Estudios/preguntas.repository";

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
    Preguntas: PreguntasRepository,
    Usuarios: UsuariosRepository
};

export default {
  get: (name) => repositories[name],
};