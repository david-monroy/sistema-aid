import conn from "../../api-connector";
import jwt from "../../../common/jwt.service";

export default {
  async agregar(data) {
    let response = await conn.post(`/estudios/`, data, jwt.getAuthHeaderToken());
    console.log(response)
    return response;
  }
};