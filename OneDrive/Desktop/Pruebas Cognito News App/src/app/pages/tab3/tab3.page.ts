import { Component, OnInit, inject } from '@angular/core';
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';
import { User } from 'src/app/models/user.model';
import { FirebaseService } from 'src/app/services/firebase.service';
import { UtilsService } from 'src/app/services/utils.service';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
})
export class Tab3Page implements OnInit {
  user: User;
  firebaseSvc = inject(FirebaseService);
  utilsSvc = inject(UtilsService);
  userSvc = inject(UserService);

  profilePicture: string | null = null;

  constructor() {}

  ngOnInit(): void {
    this.user = this.userSvc.getUser();
    this.loadProfilePicture();
  }
  
  /**
   * @function loadProfilePicture
   * @description Función que carga la imagen de usuario, esta se consume en el ngOnInit para ejecutarla 
   * cuando el usuario ingresa a la sección tab3
   */
  async loadProfilePicture() {
    if (this.user.image) {
      this.profilePicture = await this.firebaseSvc.getFilePath(this.user.image);
    }
  }

  /**
   * @function TakePicture
   * @description Funcion que por medio del plugin permite utilizar la funcionalidad nativa del celular 
   * 'Camara'
   */
  private async TakePicture(promptLabelHeader: string) {
    const image =  await Camera.getPhoto({
      quality: 90,
      allowEditing: true,
      resultType: CameraResultType.DataUrl,
      source: CameraSource.Prompt,
      promptLabelHeader,
      promptLabelPhoto: 'Selecciona una imagen',
      promptLabelPicture: 'Toma una foto',
    });

    return image;
  }

  /**
   * @function takeImage
   * @description Funcion para tomar la foto de perfil de usuario, la misma llama a la funcion interna de la
   * clase q le permite acceder a la funcionalidad del celular, guarda la imagen en firebase por medio del
   * uuid del usuario. Luego de tomar la foto, actualiza la imagen obtenida del usuario al loguearse y 
   * almacenada en el localstorage por la imagen tomada recientemente. 
   * Por medio del llamado a la funcion `presentToast` Se le muestra un mensaje de respuesta al usuario 
   * dependiendo el resultado obtenido al tomar y guardar la nueva foto de perfil. 
   */
  async takeImage() {
  
    let path = `users/${this.user.uid}`;

    const dataUrl = (await this.TakePicture('Imagen de perfil')).dataUrl;

    const loading = await this.utilsSvc.loading();
    await loading.present();

    let imagePath = `${this.user.uid}/profile`;
    this.user.image = await this.firebaseSvc.uploadImage(imagePath, dataUrl);

    this.firebaseSvc.updateDocument(path, {image: this.user.image}).then(async res => {

      this.userSvc.setUser(this.user);
      this.loadProfilePicture();
      
      this.utilsSvc.presentToast({
        message: 'Imagen guardada exitosamente',
        duration: 1500,
        color: 'success',
        position: 'middle',
        icon: 'checkmark-circle-outline'
      });
    }).catch(error => {
      console.log(error);

      this.utilsSvc.presentToast({
        message: error.message,
        duration: 2500,
        color: 'primary',
        position: 'middle',
        icon: 'alert-circle-outline'
      });
    }).finally(() => {
      loading.dismiss();
    });
  }
  
/**
 * @function signOut
 * @description Función para cerrar sesión y eliminar los datos del usuario. 
 */
  signOut() {
    this.firebaseSvc.signOut();
    this.userSvc.clearUser();
  }
}