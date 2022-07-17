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

  async cargarEncuestas(data,idEdicion) {
    let response = await conn.post(`/ediciones/cargar_encuesta/${idEdicion}`, data, headers);
    return response.data;
  }

};