import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

const headers =  {
  "Content-Type": 'multipart/form-data',
  Accept: 'multipart/form-data',
  Authorization: `Bearer ${jwt.getToken()}`
}

export default {
  async agregar(data) {
    let response = await conn.post(`/ediciones/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async validarCodigo(codigo) {
    let response = await conn.post(`/ediciones/validarCodigo`, codigo, jwt.getAuthHeaderToken());
    return response;
  },
  async consultar() {
    let response = await conn.get(`/ediciones/`, jwt.getAuthHeaderToken());
    return response;
  },
  async actualizar(id, data){
    let response = await conn.put(`/ediciones/${id}/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async eliminar(id){
    let response = await conn.delete(`/ediciones/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },

  async buscarEdicion(id){
    let response = await conn.get(`/ediciones/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async filtrar(data){
    let response = await conn.post(`/ediciones/filtrar/`, data, jwt.getAuthHeaderToken());
    return response;
  },

  async cargarEncuestas(data,idEdicion,username) {
    let response = await conn.post(`/ediciones/cargar_encuesta/${idEdicion}/${username}/`, data, headers);
    return response;
  },

  async obtenerEncuestas(idEncuesta) {
    let response = await conn.get(`/ediciones/encuestas/${idEncuesta}`, jwt.getAuthHeaderToken());
    return response.data;
  },

  async tieneEncuestas(idEncuesta) {
    let response = await conn.get(`/ediciones/tieneEncuestas/${idEncuesta}`, jwt.getAuthHeaderToken());
    return response.data;
  },

  async crearPresentacion(data) {
    let response = await conn.post(`/ediciones/crear-presentacion/`, data, jwt.getAuthHeaderToken());
    return response;
  },

  async clasificar(idEdicion) {
    let response = await conn.get(`/ediciones/clasificar/${idEdicion}/`, jwt.getAuthHeaderToken());
    return response;
  }




};