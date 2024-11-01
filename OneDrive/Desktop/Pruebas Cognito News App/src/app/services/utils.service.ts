import { Injectable, inject } from '@angular/core';
import { Router } from '@angular/router';
import {
  LoadingController,
  ToastController,
  ToastOptions,
} from '@ionic/angular';

@Injectable({
  providedIn: 'root',
})
export class UtilsService {
  loadingCtrl = inject(LoadingController);
  toastCtrl = inject(ToastController);
  router = inject(Router);

  /**
   * @function loading
   * @description Funcion para mostrar un componente de carga indicando que la funcion que se indico hacer 
   * esta en proceso. 
   */
  loading() {
    return this.loadingCtrl.create({ spinner: 'crescent' });
  }

  /**
   * presentToast
   * @description Funcion para darle feedbacks al usuario por ejecuciones exitosas o fallidas
   */
  async presentToast(opts?: ToastOptions) {
    const toast = await this.toastCtrl.create(opts);
    toast.present();
  }

  /**
   * @function routerLink
   * @description Funcion para redireccionar a distintas vistas de la aplicación
   * @param url 
   */
  routerLink(url: string) {
    return this.router.navigateByUrl(url);
  }

  /**
   * @function saveInLocalStorage
   * @description Funcion para guardar informacion en el local storage
   * @params key, value 
   */
  saveInLocalStorage(key: string, value: any) {
    return localStorage.setItem(key, JSON.stringify(value));
  }

  /**
   * @function getFromLocalStorage
   * @description Funcion para obtener informacion almacenada en el local storage
   * @param key 
   */
  getFromLocalStorage(key: string) {
    return JSON.parse(localStorage.getItem(key));
  }
}