import { Injectable } from "@angular/core";
import { User } from "../models/user.model";

@Injectable({
    providedIn: 'root',
})

/**
 * @descripcion Servicio creado para el manejo de datos de usuario desde todo el proyecto
 */
export class UserService {
    private user: User | null = null;

    /**
     * @function setUser
     * @description Función para guardar los datos del usuario en la entidad User
     */
    setUser(user: User): void {
        this.user = user;
    }

    /**
     * @function getUser
     * @description Función para obtener los datos del usuario de la entidad User
     */
    getUser(): User | null {
        return this.user;
    }

    /**
     * @function clearUser
     * @description Función para eliminar los datos del usuario de la entidad User
     */
    clearUser() : void {
        this.user = null;
    }
}