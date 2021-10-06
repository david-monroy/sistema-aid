import conn from "../api-connector";
import jwt from "../../common/jwt.service";

export default {
  async agregar(data){
    let response = await conn.post(`/participantes/`, data, jwt.getAuthHeaderToken());
    return response;
  },
  async obtener(){
    let response = await conn.get(`/participantes/`, jwt.getAuthHeaderToken());
    return response;
  },
  async eliminar(id){
    let response = await conn.delete(`/participantes/${id}/`, jwt.getAuthHeaderToken());
    return response;
  },
  async filtrar(data){
    let response = await conn.post(`/participantes/filtrar`, data, jwt.getAuthHeaderToken());
    return response;
  },
};
