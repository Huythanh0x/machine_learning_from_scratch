/**
 * Created by goran on 1/10/2017.
 */

// create interface Shooter with method reload
// implement that interface on classes Pistolero and Archer
// pistolero already has reload method so there is nothing to implement
// archer does not have reload method you have to implement it
// use same logic from reload method in pistolero class
// fix attack logic in Archer attack method so archer reloads when there are no more arrows
// when archer reloads print message archer reloading
// run and check console to see if archer is reloading

enum EnemyClassType {
    LIGHT,
    HEAVY;

    public boolean isLight() {
        return this == LIGHT;
    }

    public boolean isHeavy() {
        return this == HEAVY;
    }
}

interface Shooter {
    void reload();
}

interface Healable {
    void heal(int amount);
}

abstract class Enemy {
    private int health;
    private String weapon;
    private int damage;
    private EnemyClassType type = EnemyClassType.LIGHT;

    protected Enemy(int health, String weapon) {
        this.health = health;
        this.weapon = weapon;
        System.out.println("Enemy constructor called");
    }

    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        if (health < 0) {
            health = 0;
        }

        if (health > 100) {
            health = 100;
        }

        this.health = health;
    }

    public String getWeapon() {
        return weapon;
    }

    public void setWeapon(String weapon) {
        this.weapon = weapon;
    }

    public int getDamage() {
        return damage;
    }

    public void setDamage(int damage) {
        this.damage = damage;
    }

    public EnemyClassType getType() {
        return type;
    }

    public void setType(EnemyClassType type) {
        this.type = type;
    }

    public void attack(Enemy enemy) {
        int percantage = (int)(damage * 0.1); // 10% of damage
        int damageToTake = damage;

        /*
        if(type == EnemyClassType.LIGHT && enemy.type == EnemyClassType.HEAVY) { // light vs heavy
            damageToTake = damage - percantage; // 10% less
        } else if(type == EnemyClassType.HEAVY && enemy.type == EnemyClassType.LIGHT) { // heavy vs ligth
            damageToTake = damage + percantage; // 10% more
        }
        */

        /*
        if(type.isLight() && enemy.type.isHeavy()) { // light vs heavy
            damageToTake = damage - percantage; // 10% less
        } else if(type.isHeavy() && enemy.type.isLight()) { // heavy vs ligth
            damageToTake = damage + percantage; // 10% more
        }
        */

        if(isLight() && enemy.isHeavy()) { // light vs heavy
            damageToTake = damage - percantage; // 10% less
        } else if(isHeavy() && enemy.isLight()) { // heavy vs ligth
            damageToTake = damage + percantage; // 10% more
        }

        System.out.println("attacking " + enemy.getClass().getSimpleName() + " with " + weapon);
        enemy.takeDamage(damageToTake);
    }

    public boolean isLight() {
        return type.isLight();
    }

    public boolean isHeavy() {
        return type.isHeavy();
    }

    public void takeDamage(int damageToTake) {
        setHealth(health - damageToTake);
    }

    public abstract void run();

//    public void attack(Archer archer) {}
//    public void attack(Pikeman pikeman) {}
}

class Pikeman extends Enemy {

    private int armor;

    public Pikeman(int health, int armor) {
        super(health, "pike");
        this.armor = armor;
        setType(EnemyClassType.HEAVY);
        System.out.println("Pikeman constructor called");
    }

    public int getArmor() {
        return armor;
    }

    public void setArmor(int armor) {
        this.armor = armor;
    }

    @Override
    public void run() {
        System.out.println("pikeman running");
    }
}

class Archer extends Enemy implements Shooter {

    private int arrowCount;

    public Archer(int health, int arrowCount) {
        super(health, "bow");
        this.arrowCount = arrowCount;
        System.out.println("Archer constructor called");
    }

    public int getArrowCount() {
        return arrowCount;
    }

    public void setArrowCount(int arrowCount) {
        this.arrowCount = arrowCount;
    }

    @Override
    public void attack(Enemy enemy) {
        if (arrowCount <= 0) {
            reload();
        }

        super.attack(enemy);
        arrowCount--;
        System.out.println("arrows left= " + arrowCount);
    }

    @Override
    public void run() {
        System.out.println("archer running");
    }

    @Override
    public void reload() {
        if (arrowCount <= 0) {
            System.out.println("archer reloading");
            arrowCount = 1;
        }
    }
}

class Pistolero extends Enemy implements Healable, Shooter {

    private int bulletCount = 6;

    public Pistolero(int health) {
        super(health, "pistol");
    }

    @Override
    public void attack(Enemy enemy) {
        if (bulletCount <= 0) {
            reload();
        }

        super.attack(enemy);
        System.out.println("firing bullet at " + enemy.getClass().getSimpleName());
        bulletCount--;
        System.out.println("bulletCount= " + bulletCount);
    }

    @Override
    public void reload() {
        if (bulletCount <= 0) {
            System.out.println("reloading");
            bulletCount = 6;
        }
    }

    @Override
    public void run() {
        System.out.println("pistolero running");
    }

    @Override
    public void heal(int amount) {
        if (amount < 0) {
            System.out.println("cant heal with negative amount");
            return;
        }

        System.out.println("healing amount= " + amount);
        setHealth(getHealth() + amount);
    }
}

public class LibGdx {

    public static void main(String[] args) {
//        Enemy enemy = new Enemy();

        Enemy pikeman = new Pikeman(100, 100);
        pikeman.run();
        pikeman.setDamage(15);

        Enemy archer = new Archer(100, 5);
        archer.run();
        archer.setDamage(10);

        Enemy pistolero = new Pistolero(100);
        pistolero.run();
        pistolero.setDamage(20);

        System.out.println("pikeman Type= " + pikeman.getType());
        System.out.println("archer Type= " + archer.getType());
        System.out.println("pistolero Type= " + pistolero.getType());

        System.out.println("pikeman heavy= " + pikeman.isHeavy() + " light= " + pikeman.isLight());
        System.out.println("archer heavy= " + archer.isHeavy() + " light= " + archer.isLight());
        System.out.println("pistolero heavy= " + pistolero.isHeavy() + " light= " + pistolero.isLight());

        pikeman.attack(archer);
        archer.attack(pikeman);
        System.out.println("pikeman health= " + pikeman.getHealth() + " archer health= " + archer.getHealth());

        pikeman.attack(pistolero);
        pistolero.attack(pikeman);
        System.out.println("pikeman health= " + pikeman.getHealth() + " pistolero health= " + pistolero.getHealth());

        archer.attack(pistolero);
        pistolero.attack(archer);
        System.out.println("archer health= " + archer.getHealth() + " pistolero health= " + pistolero.getHealth());

    }
}