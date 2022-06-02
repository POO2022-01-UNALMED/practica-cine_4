package gestorAplicacion;

import java.util.ArrayList;

public class Funcionalidades {
    public ArrayList<Sala>inicializarSalas(Cartelera cartelera, ArrayList<Trabajador> trabajadoresPlanta){
        int numeroSillas;
        numeroSillas = 240;

        ArrayList<Silla> sillas = new ArrayList<Silla>();
        ArrayList<Sala> salas = new ArrayList<Sala>();
        ArrayList<Trabajador> trabajadores = new ArrayList<Trabajador>();
        Cliente varInicializacionCliente = new Cliente(100065534, 0, "NA", "NA", 0, 0);
    
        for (int i = 0; i < numeroSillas; i++) {
            if (i>=0 && i<=80) {
                Silla silla = new Silla(i, "Economica", "Lateral Izquierdo",varInicializacionCliente);
                sillas.add(silla);

                
            } 
            else if (i>=80 && i<=160) {
                Silla silla = new Silla(i, "Vip", "Central",varInicializacionCliente);
                sillas.add(silla);

                
            }
            else if (i>=160 && i<=240) {
                Silla silla = new Silla(i, "Economica", "Lateral derecho",varInicializacionCliente);
                sillas.add(silla);


            }
            
        }



        int varNumeroSalas;
        varNumeroSalas = 10;
        ArrayList<Pelicula> varPelis = new ArrayList<Pelicula>();
        varPelis = cartelera.getPelis();
        for (int index = 0; index < varNumeroSalas; index++) {
            trabajadores.add(trabajadoresPlanta.get(index));

            if(index>0 && index<5){
                Sala sala = new Sala("3D", sillas, varPelis.get(index),trabajadores,index,0);
                salas.add(sala);
            }
            else{
                Sala sala = new Sala("2D", sillas, varPelis.get(index),trabajadores,index,0);
                salas.add(sala);
            }
            trabajadores = new ArrayList<Trabajador>();
        }
        return salas;

    }

    public Cartelera inicializarCartelera(){
        ArrayList<Pelicula> pelis = new ArrayList<>();
        Pelicula peli1 = new Pelicula("La caida de la casa blanca", "Roland Emmerich", 2013, 131, "Accion", "Estados unidos", "+14",15);
        Pelicula peli2 = new Pelicula("Ciudad de Dios", "Fernando Meirelles", 2002, 130, "Accion", "Brasil", "+18",15);
        Pelicula peli3 = new Pelicula("Terminator","James Cameron", 1984, 108, "Ciencia ficcion","Estados unidos", "+16",20);
        Pelicula peli4 = new Pelicula("Salvando al soldado Ryan", "Steven Spielberg", 1998, 169, "Belico","Estados Unidos", "+16",15);
        Pelicula peli5 = new Pelicula("Matrix", "Hermanas Wachowski", 2001, 136, "Ciencia ficcion", "Estados unidos", "+16",20);
        Pelicula peli6 = new Pelicula("Robots", "Chris Wedge", 2005, 84, "Animacion", "Estados unidos", "+4",20);
        Pelicula peli7 = new Pelicula("Enemigo a las puertas", "Jean-Jacques Annaud", 2001, 131, "Accion", "Estados unidos", "+16",20);
        Pelicula peli8 = new Pelicula("Interstellar  ", "Christopher Nolan", 2014, 169,"Ciencia ficcion","Estados undidos", "+13",20);
        Pelicula peli9 = new Pelicula("The Godfather", "Francis Ford Coppola", 1972, 177, "Gangsters", "Estados unidos", "+16",20);
        Pelicula peli10 = new Pelicula("El gran hotel budapest", "Wes Anderson", 2014, 99, "Comedia", "Estados unidos", "+16",20);
        pelis.add(peli1); pelis.add(peli2); pelis.add(peli3); pelis.add(peli4); pelis.add(peli5); pelis.add(peli6); pelis.add(peli7); pelis.add(peli8); pelis.add(peli9);pelis.add(peli10);
        Cartelera cartelera = new Cartelera(pelis);
        return cartelera;
    }


    public ArrayList<Trabajador> inicializarTrabajdores(){
        ArrayList<Trabajador> trabajadores = new ArrayList<>();
        Trabajador trabajador1 = new Trabajador(100053321, 310402011, "Jaime Lozano", "M", 34, "Administrador", true);
        Trabajador trabajador2 = new Trabajador(101012342, 310401233, "Kevin Duran", "M", 36, "Empleado de planta", false);
        Trabajador trabajador3 = new Trabajador(105123423, 310501232, "Juan Alzate", "M", 24, "Empleado de planta", false);
        Trabajador trabajador4 = new Trabajador(106421321, 305123214, "Maria Dos Santos", "F", 26, "Empleado de planta", false);
        Trabajador trabajador5 = new Trabajador(107421321, 305231234, "Alex Castano", "M", 29, "Empleado de planta", false);
        Trabajador trabajador6 = new Trabajador(101232134, 310452122,"Alejandro Sanchez" , "M", 42, "Empleado de servicio", false);
        Trabajador trabajador7 = new Trabajador(106121321, 306232123, "Juan Castrillon", "M", 23, "Empleado de planta", false);
        Trabajador trabajador8 = new Trabajador(102135231, 305324231, "Mariana Carillo", "F", 29, "Empleado de planta", false);
        Trabajador trabajador9 = new Trabajador(10432521, 342151232, "Cindy Perez", "F", 24, "Empleado de planta", false);
        Trabajador trabajador10 = new Trabajador(107421321, 305231234, "Juanita Gomez", "F", 33, "Empleado de planta", false);
        Trabajador trabajador11 = new Trabajador(104324321, 310331234, "Manuel Ortega", "M", 24, "Empleado de planta", false);
        Trabajador trabajador12 = new Trabajador(107421321, 305231234, "Alex Castano", "M", 27, "Empleado de planta", false);
        Trabajador trabajador13 = new Trabajador(107421321, 306233234, "Manuela Ortega", "M", 25, "Empleado de servicio", false);




        trabajadores.add(trabajador1);trabajadores.add(trabajador2);trabajadores.add(trabajador3);trabajadores.add(trabajador4);trabajadores.add(trabajador5);trabajadores.add(trabajador6);
        trabajadores.add(trabajador7);trabajadores.add(trabajador8);trabajadores.add(trabajador9);trabajadores.add(trabajador10);trabajadores.add(trabajador11);trabajadores.add(trabajador12);trabajadores.add(trabajador13);
        return trabajadores;
    }
    
    public ArrayList<Trabajador> trabajdoresEmpleadosPlanta( ArrayList<Trabajador> trabajadores){
        ArrayList<Trabajador> varTrabajadores = trabajadores;
        varTrabajadores.remove(0); 
        varTrabajadores.remove(4);
        varTrabajadores.remove(10);

        return varTrabajadores;

    

    }

    
}


