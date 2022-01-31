import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

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
  async filtrar(data){
    let response = await conn.post(`/ediciones/filtrar/`, data, jwt.getAuthHeaderToken());
    return response;
  },

};