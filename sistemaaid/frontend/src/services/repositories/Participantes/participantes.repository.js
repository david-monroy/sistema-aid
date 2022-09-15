import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async agregar(data){
    let response = await conn.post(`/participantes/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async obtener(){
    let response = await conn.get(`/participantes/`, jwt.getAuthHeaderToken());
    return response;
  },
  async obtenerPorId(id){
    let response = await conn.get(`/participantes/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async obtenerEncuestas(id){
    let response = await conn.get(`/participantes/obtenerEncuestas/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async actualizar(id, data){
    let response = await conn.put(`/participantes/${id}/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async eliminar(id){
    let response = await conn.delete(`/participantes/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async filtrar(data){
    let response = await conn.post(`/participantes/filtrar/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async cargaMasiva(data){
    let response = await conn.post(`/participantes/carga_masiva/`, data, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }, jwt.getAuthHeaderToken());
    return response;
  },
  async editarMasivo(data){
    let response = await conn.post(`/participantes/editar_masivo/`, data, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }, jwt.getAuthHeaderToken());
    return response;
  },
};
