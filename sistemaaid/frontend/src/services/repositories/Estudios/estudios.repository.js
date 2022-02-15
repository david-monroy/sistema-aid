import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async agregar(data) {
    let response = await conn.post(`/estudios/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async consultar() {
    let response = await conn.get(`/estudios/`, jwt.getAuthHeaderToken());
    return response;
  },
  async obtenerEdiciones(id) {
    let response = await conn.get(`/estudios/ediciones/${id}`, jwt.getAuthHeaderToken());
    return response;
  },
  async validarCodigo(codigo) {
    let response = await conn.post(`/estudios/validarCodigo`, codigo, jwt.getAuthHeaderToken());
    return response;
  }
};