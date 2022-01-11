import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async agregar(data) {
    console.log(data);
    let response = await conn.post(`/ediciones/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async validarCodigo(codigo) {
    let response = await conn.post(`/ediciones/validarCodigo`, codigo, jwt.getAuthHeaderToken());
    return response;
  }

};