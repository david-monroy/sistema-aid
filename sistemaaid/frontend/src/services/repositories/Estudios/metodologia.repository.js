import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async insertarMetodologia(data) {
    let response = await conn.post(`/metodologia/`, data, jwt.getAuthHeaderToken());
    return response;
  },

  async actualizar(id, data){
    let response = await conn.put(`/metodologia/${id}/`, data, jwt.getAuthHeaderToken());
    return response;
  },

  async buscarMetodologia(idEdicion) {
    let response = await conn.get(`/metodologia/buscar/${idEdicion}/`,jwt.getAuthHeaderToken());
    return response[0];
  },

};