
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
                        System.out.print("3.Buscar una reserva \n");
                        System.out.println("4.Inicializar Cine (Reservada para un unico uso)");
                        System.out.println("5.Verificar integridad de las salas");                       
                        System.out.println("6.Hacer devolucion");
                        System.out.print("7.Salir\n\n");
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
                                        System.out.println("Para elegir la pelicula ingrese un numero del 1 al 10");
                                        int peli = entrada.nextInt()-1;
                                        funcionalidades.danarSilla(peli, salas);
                                        System.out.println("Para la silla escoja un numero del 1 al 240");
                                        int silla = entrada.nextInt()-1;
                                        System.out.println(funcionalidades.asiganarCliente(peli, silla, cliente1, salas));
                                        



                                    }
                                    else{
                                        System.out.println(" ");
                                        System.out.println("Que pelicula desea ver? ");
                                        System.out.println("Para elegir la pelicula ingrese un numero del 1 al 10");
                                        int peli = entrada.nextInt()-1;
                                        System.out.println("Para la silla escoja un numero del 1 al 240");
                                        int silla = entrada.nextInt()-1;
                                        System.out.println(funcionalidades.asiganarCliente(peli, silla, cliente1, salas));
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
                                 System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
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
                                        String cambiar = entrada.nextLine();
                                        System.out.println("Ingrese nombre de la pelicula nueva");
                                        String a =entrada.nextLine();
                                        System.out.println("Ingrese director de la pelicula nueva");
                                        String director =entrada.nextLine();
                                        System.out.println("Ingrese ano de la pelicula nueva");
                                        int ano = entrada.nextInt();
                                        System.out.println("Ingrese duracion de la pelicula nueva");
                                        int duracion = entrada.nextInt();
                                        System.out.println("Ingrese genero de la pelicula nueva");
                                        String genero =entrada.nextLine();
                                        entrada.nextLine();
                                        System.out.println("Ingrese pais de la pelicula nueva");
                                        String pais =entrada.nextLine();
                                        System.out.println("Ingrese calificacion de la pelicula nueva");
                                        String calificacion =entrada.nextLine();
                                        System.out.println("Ingrese precio de la pelicula nueva");
                                        int precio = entrada.nextInt();
                                        Pelicula peli=new Pelicula( a,  director,  ano,  duracion,  genero,  pais,  calificacion,  precio);
                                        System.out.println(cartelera.cambiarPelicula(a, peli, cartelera));

                                    }

                                    
                                } else {
                                    System.out.println(" ");
                                    Cartelera.imprimirCartelera(cartelera);
                                }
                                

                                 System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
                                break;



                            case 3:
                                System.out.println("Ingresa la cedula para buscar los datos de la reserva del cliente (No mas de 9 digitos)");
                                int varLocalizarClienteCedula = entrada.nextInt();                             
                                Cliente varBuscquedaCliente = new Cliente(varLocalizarClienteCedula, 0, "NA", "NA", 0, 0);
                                if (!varBuscquedaCliente.loging(varBuscquedaCliente , clientes)) {
                                    System.out.println("El cliente no esta registrado");}
                                else{
                                    varBuscquedaCliente.localizacionCliente(salas, varLocalizarClienteCedula);
                                }
                                 System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
                                break;
                            
                                

                            case 4:
                                cartelera = funcionalidades.inicializarCartelera();
                                salas = funcionalidades.inicializarSalas(cartelera);
                                System.out.println("Se ha iniciado existosamente las salas");
                                trabajadores = funcionalidades.inicializarTrabajdores();
                                salas = funcionalidades.agregarTrabajadores(salas,trabajadores);
                                System.out.println("Se ha inicializado correctamente el cine");
                                 System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
                                break;
                            
                            
                            case 5:
                               
                                System.out.print("\n\t.:Integridad de Sala:.\t\n");
                               System.out.print("1.Ver estado de la silla \n");
                               System.out.print("2.Modificar el estado de la silla\n");
                               
                               int opcione = entrada.nextInt();
                               
                                      
                               if(opcione==1){
                                   System.out.print("Ingrese numero de la sala \n");
                                   int sala = entrada.nextInt();
                                   System.out.print("Ingrese numero de la silla \n");
                                   
                                   System.out.print(funcionalidades.vericarSilla(sala, salas));
                                   
                                   
                               }
                               else{
                                   System.out.print("1.Reparar silla \n");
                                   System.out.print("2.Danar silla \n");
                                   int opcion1 = entrada.nextInt();
                                   if (opcion1==1){
                                       System.out.print("Ingrese numero de la sala \n");
                                       int sala = entrada.nextInt();
                                       System.out.print("Ingrese numero de la silla \n");
                                       int silla = entrada.nextInt();
                                       System.out.print(funcionalidades.arreglarSilla(sala, silla, salas));
                                   }else{
                                       System.out.print("Ingrese numero de la sala \n");
                                       int sala = entrada.nextInt();
                                       System.out.print("Ingrese numero de la silla \n");
                                       int silla = entrada.nextInt();
                                       System.out.print(funcionalidades.danarSilla(sala,silla, salas));
                                   }
                            
                               }
                               System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
                               
                               int salir = entrada.nextInt();
                               if (salir==1){
                                   break;
                               }else{
                                   break;
                               }

                            case 6:
                                System.out.println("Ingresa la cedula para buscar los datos de la reserva del cliente (No mas de 9 digitos)");
                                int a = entrada.nextInt();                             
                                Cliente cli = new Cliente(a, 0, "NA", "NA", 0, 0);
                                if (!cli.loging(cli , clientes)) {
                                    System.out.println("El cliente no esta registrado");}
                                else{
                                    System.out.print(funcionalidades.devolucion(cli, salas));
                                }
                               System.out.print("\n\t.:Volver al menu:.\t\n");
                               System.out.print("1. si\n");
                               System.out.print("2. no\n");
                               salir = entrada.nextInt();
                               if (salir==1){
                                   break;
                               }else{
                                   break;
                               }
                                   

                            case 7:
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

