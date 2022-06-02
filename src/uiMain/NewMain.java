package uiMain;
import gestorAplicacion.*;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author usuario
 */
public class NewMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        ArrayList<Cliente> clientes = new ArrayList<Cliente>();
        ArrayList<Trabajador> trabajadores = new ArrayList<Trabajador>();
        ArrayList<Trabajador> varTrabajadores = new ArrayList<Trabajador>();

        ArrayList<Sala> salas = new ArrayList<Sala>();
        Cartelera cartelera = new Cartelera(null );
        Funcionalidades funcionalidades =new Funcionalidades();
        

        try (Scanner entrada = new Scanner(System.in)) {
            int opcion = 0;
            int varloging;

            System.out.println("Bienvenido al cine JKS, ingrese la contrasena para ingresar al menu: ");
            varloging = entrada.nextInt();
            if (varloging == 0000) {
                opcion = 0;
                    while (opcion != 9) {
                        System.out.print("\n\t.:Menu:.\t\n");
                        System.out.print("1.Comprar boleteria \n");
                        System.out.print("2.Editar la cartelera, o imprimir cartelera\n");
                        System.out.print("3.Buscar o eliminar registro de un Trabajador \n"); //Discutir agregar
                        System.out.print("4.Buscar una reserva \n");
                        System.out.println("5.Inicializar Cine (Reservada para un unico uso)");
                        System.out.println("6.Verificar integridad de las salas");
                        System.out.println("7.Enviar a servicios a barrer una sala");
                        System.out.println("8.Hacer devolucion");
                        System.out.print("9.Salir\n\n");
                        System.out.print("Opcion: ");


                        opcion = entrada.nextInt();
                        switch (opcion) {
                            case 1:
                                System.out.println("Ingrese la cedula del cliente \nCedula no mas de 9 digitos");
                                int cedula = entrada.nextInt();

                                System.out.println("Ingrese el nombre del cliente \nNombre seguido de espacio y un apellido");
                                String nombre = entrada.nextLine();
                                entrada.nextLine();

                                Cliente cliente = new Cliente(cedula,000,nombre,"Na",0,0);

                                if (!cliente.loging(cliente, clientes)) {
                                    System.out.println("El cliente no esta registrado, se debe registrar para comprar boleteria");

                                    System.out.println("Ingrese el celular, \nCelular no mas de 9 digitos, Para agregar el cliente, ingrese el celular");
                                    int celular = entrada.nextInt();

                                    System.out.println("Sexo M o F");
                                    String sexo = entrada.next();

                                    System.out.println("Ingrese la edad, para agregar el cliente,edad minimo 16 para registro");
                                    int edad = entrada.nextInt();

                                    Cliente cliente1 = new Cliente(cedula,celular,nombre,sexo,edad,0);
                                    clientes.add(cliente1);

                                    System.out.println("Se ha registrado satisfactoriamente al cliente \nDesea imprimir la cartelera? 1 si, 2 no");
                                    int varOpcionPrint = entrada.nextInt();
                                    if(varOpcionPrint == 1){
                                        Cartelera.imprimirCartelera(cartelera);
                                        System.out.println(" ");
                                        System.out.println("Que pelicula desea ver? ");
                                        System.out.println("Para elegir la pelicula todo miniscula");
                                        String varElegirPeli = entrada.nextLine();



                                    }
                                    else{
                                        System.out.println("Que pelicula desea ver");
                                    }
                                    
                                    
                                } 
                                else {
                                    System.out.println("El cliente esta registrado");
                                    System.out.println("Desea imprimir la cartelera? 1 si, 2 no");
                                    int varOpcionPrint = entrada.nextInt();
                                    if(varOpcionPrint == 1){
                                        Cartelera.imprimirCartelera(cartelera);
                                    }
                                    else{
                                        System.out.println("Que pelicula desea ver");
                                    }                                                                  
                                }
                                break;


                            case 2:
                                System.out.println("Desea cambiar o imprimir cartelera? \n1 para cambiar, 2 para imprimir la cartelera");
                                int varOpcion = entrada.nextInt();
                                if (varOpcion == 1) {
                                    boolean varVerificarExistencia = false;
                                    System.out.println("Que pelicula desea cambiar? \nPara cambiar ingrese el nombre de la pelicula (Todo miniscula) ");
                                    entrada.nextLine();
                                    String varEntrada = entrada.nextLine();
                                    varVerificarExistencia = cartelera.confirmarPelicula(cartelera, varEntrada);
                                    if (varVerificarExistencia == true) {
                                        System.out.println("La pelicula ya existe");
                                        
                                    } else if(varVerificarExistencia == false) {
                                        System.out.println("La pelicula no esta");
                                        System.out.println("Ingrese la pelicula que sea cambiar");

                                    }

                                    
                                } else {
                                    System.out.println(" ");
                                    Cartelera.imprimirCartelera(cartelera);
                                }
                                


                                break;



                            case 3:
                                break;



                            case 4:
                                System.out.println("Ingresa la cedula para buscar los datos de la reserva del cliente (No mas de 9 digitos)");
                                int varLocalizarClienteCedula = entrada.nextInt();                             
                                Cliente varBuscquedaCliente = new Cliente(varLocalizarClienteCedula, 0, "NA", "NA", 0, 0);
                                if (!varBuscquedaCliente.loging(varBuscquedaCliente , clientes)) {
                                    System.out.println("El cliente no esta registrado");}
                                else{
                                    varBuscquedaCliente.localizacionCliente(salas, varLocalizarClienteCedula);
                                }
                                break;
                            
                                

                            case 5:
                                cartelera = funcionalidades.inicializarCartelera();
                                trabajadores = funcionalidades.inicializarTrabajdores();
                                varTrabajadores = funcionalidades.trabajdoresEmpleadosPlanta(trabajadores);
                                salas = funcionalidades.inicializarSalas(cartelera,varTrabajadores);
                                System.out.println("Se ha iniciado existosamente las salas");
                                System.out.println("Se ha inicializado correctamente el cine");
                                break;
                            case 6:
                                
                                break;
                            
                            case 7:
                                break;

                            case 8:
                                break;


                            case 9:
                                break;


                            default:
                                System.out.println("Opción errada\n");
                        }
                    }
            }
            else {
                System.out.println("Clave incorrecta hasta luego");
            }
        }
    }
}

