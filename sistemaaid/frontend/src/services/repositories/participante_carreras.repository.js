import conn from "../api-connector";
import jwt from "../../common/jwt.service";

export default {
  async agregar(data){
    let response = await conn.post(`/participantecarreras/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async obtener(){
    let response = await conn.get(`/participantecarreras/`, jwt.getAuthHeaderToken());
    return response;
  }
};
