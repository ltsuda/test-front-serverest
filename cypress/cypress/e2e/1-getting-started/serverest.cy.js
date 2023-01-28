describe("example serverest", () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000");
    });

    it("has title", () => {
        cy.title().should("eq", "Front - ServeRest");
    });
});
