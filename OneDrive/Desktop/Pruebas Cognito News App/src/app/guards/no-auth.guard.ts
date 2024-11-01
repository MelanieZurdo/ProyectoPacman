import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { FirebaseService } from '../services/firebase.service';
import { Injectable, inject } from '@angular/core';
import { UtilsService } from '../services/utils.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class NoAuthGuard implements CanActivate {

  firebaseSvc = inject(FirebaseService);
  utilSvc = inject(UtilsService);
 /**
  * @function canActivate
  * @description Funcion que verifica si existe un usuario logueado, en caso de existir permite al usuario 
  * ingresar al sistema y lo redirige a la sección de tabs.
  */
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      
    return new Promise((resolve) => {

      this.firebaseSvc.getAuth().onAuthStateChanged((auth) => {

        if (!auth) {
          resolve(true);
        } else {
          this.utilSvc.routerLink('tabs');
          resolve(false);
        }
      });
    });
  }
}
