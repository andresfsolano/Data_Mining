library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Logic_Circuit is
    Port ( A, B : in STD_LOGIC; -- Binary input 
		   SEL : in STD_LOGIC_VECTOR (1 downto 0); -- Two digit's binary selector 
		   Z : out STD_LOGIC);
end Logic_Circuit;

architecture Behavioral of Logic_Circuit is
begin
	process (SEL, A, B)
		begin
			case SEL is
				when "00" => Z <= A OR B;
				when "01" => Z <= A AND B;
				when "10" => Z <= A XOR B;
				when "11" => Z <= A NAND B;
				-- Default state to guarantee the proper case execution
				when others => Z <= '0';
			end case;
	end process;

end Behavioral;